declare function seasonsFetch(): seasonData[];
type seasonData = {
    accomplishments: string[],
    description: string,
    end: string,
    id: string,
    members: string[],
    modifications: {
        name: string,
        type: string,
        url: string
    }[],
    name: string,
    start: string,
    timestamp: number,
    version: string
};
type statusResponse = {
    members: {
        id: string,
        name: string,
        properties: [ { name: "textures", value: string, signature?: string } ]
    }[],
    ping: number,
    timestamp: number
};